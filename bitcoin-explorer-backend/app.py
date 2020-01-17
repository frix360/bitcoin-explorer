from flask import Flask, jsonify, request, abort
from bitcoin.rpc import RawProxy

from JsonEncoder import JsonEncoder
from search_functions import collect_search_functions

app = Flask(__name__)
app.json_encoder = JsonEncoder
@app.after_request  # blueprint can also be app~~
def before_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/getBlockchainInfo', methods=['GET'])
def get_blockchain_info():
    p = RawProxy()
    # Run the getblockchaininfo command, store the resulting data in info
    blockchain_info = p.getblockchaininfo()

    filtered_info = {
        "chainType": blockchain_info["chain"],
        "blockCount": blockchain_info["blocks"],
        "validatedHeadersCount": blockchain_info["headers"],
        "difficulty": str(blockchain_info["difficulty"]),
        "verificationProgress": str(blockchain_info["verificationprogress"] * 100),
        "bestBlockHash": str(blockchain_info["bestblockhash"])
    }

    return jsonify(filtered_info)


@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query')

    funcs = collect_search_functions(query)

    for func in funcs:
        result = func(query)
        if result is not None:
            return result

    abort(404)


@app.route('/api/getLatestBlocks', methods=['GET'])
def get_latest_blocks():
    p = RawProxy()
    blocks_to_take = 10
    if request.args.get('count'):
        blocks_to_take = int(blocks_to_take)
    blocks_count = p.getblockcount()
    block_heights = list(range(blocks_count - blocks_to_take, blocks_count))
    block_hashes = list(map(p.getblockhash, block_heights))
    block_hashes.reverse() # So latest hashes would go first
    return jsonify(block_hashes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6457)
