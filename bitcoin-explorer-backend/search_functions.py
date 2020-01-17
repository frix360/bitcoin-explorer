from bitcoin.rpc import RawProxy


def search_for_block_by_height(height):
    p = RawProxy()
    try:
        int_height = int(height)
        block_hash = p.getblockhash(int_height)
        return search_for_block_by_header(block_hash)
    except:
        return None


def search_for_block_by_header(header):
    p = RawProxy()
    try:
        block_info = p.getblock(header)
        block_info['resulttype'] = 'block'
        return block_info
    except:
        return None


def search_for_transaction_by_txid(txid):
    p = RawProxy()
    try:
        transaction_info = p.getrawtransaction(txid, True)
        transaction_info['resulttype'] = 'transaction'
        return transaction_info
    except:
        return None


def collect_search_functions(query):
    funcs = []
    if len(query) < 64:
        funcs.append(search_for_block_by_height)
    else:
        funcs.append(search_for_transaction_by_txid)
        funcs.append(search_for_block_by_header)
    return funcs
