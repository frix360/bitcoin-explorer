<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>Current blockchain info</v-card-title>
          <v-card-text>
            <v-container style="text-align: center" fluid>
              <v-row>
                <v-col>
                  <v-card outlined>
                    <v-card-title>Network type:</v-card-title>
                    <v-card-text class="headline font-weight-bold">{{
                      blockchainInfo.chainType
                    }}</v-card-text>
                  </v-card>
                </v-col>
                <v-col>
                  <v-card outlined>
                    <v-card-title>Block count:</v-card-title>
                    <v-card-text class="headline font-weight-bold">{{
                      blockchainInfo.blockCount
                    }}</v-card-text>
                  </v-card>
                </v-col>
                <v-col>
                  <v-card outlined>
                    <v-card-title>Validated blocks:</v-card-title>
                    <v-card-text class="headline font-weight-bold">{{
                      blockchainInfo.validatedHeadersCount
                    }}</v-card-text>
                  </v-card>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="2">
                  <v-card style="height: 100%" outlined>
                    <v-card-title>Difficulty:</v-card-title>
                    <v-card-text class="subtitle-1 font-weight-bold">{{
                      blockchainInfo.difficulty
                    }}</v-card-text>
                  </v-card>
                </v-col>
                <v-col cols="2">
                  <v-card style="height: 100%" outlined>
                    <v-card-title>Verification status:</v-card-title>
                    <v-card-text class="subtitle-2 font-weight-bold"
                      >{{ blockchainInfo.verificationProgress }}%</v-card-text
                    >
                  </v-card>
                </v-col>
                <v-col>
                  <v-card outlined>
                    <v-card-title>Best block hash:</v-card-title>
                    <v-card-text
                      @click="(e) => search(blockchainInfo.bestBlockHash)"
                      class="headline font-weight-bold"
                      style="cursor: pointer"
                      >{{ blockchainInfo.bestBlockHash }}</v-card-text
                    >
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="7">
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Search:</v-card-title>
              <v-card-text>
                <v-row>
                  <v-col cols="10">
                    <v-text-field
                      autocomplete="off"
                      v-model="searchValue"
                      clearable
                      label="Search for block header hash, block height or txid..."
                    ></v-text-field>
                  </v-col>
                  <v-col
                    style="text-align: center"
                    align-self="center"
                    cols="2"
                  >
                    <v-btn @click="(e) => search()" color="primary"
                      >Search</v-btn
                    >
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <v-row v-if="searchResult">
          <v-col>
            <component
              :is="getResultType(searchResult)"
              :result-data="searchResult"
              @hashClicked="(e) => search(e)"
            ></component>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="5">
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Latest blocks</v-card-title>
              <v-card-text>
                <v-list>
                  <v-list-item
                    v-for="hash in latestBlocks"
                    @click="(e) => search(hash)"
                  >
                    {{ hash }}
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import BlockResult from '../components/BlockResult'
import TransactionResult from '../components/TransactionResult'

export default {
  data() {
    return {
      blockchainInfo: {},
      latestBlocks: [],
      searchValue: '',
      searchResult: null
    }
  },
  components: {
    BlockResult,
    TransactionResult
  },
  mounted() {
    this.loadBlockchainInfo()
  },
  methods: {
    async loadBlockchainInfo() {
      this.blockchainInfo = await this.$axios.$get('/getBlockchainInfo')
      this.latestBlocks = await this.$axios.$get('/getLatestBlocks')
    },
    async search(value) {
      if (!this.searchValue && !value) {
        alert('Search field is empty!')
        return
      }
      if (value) this.searchValue = value

      try {
        this.searchResult = await this.$axios.$get('/search', {
          params: {
            query: this.searchValue
          }
        })
      } catch (e) {
        alert('Could not find anything!')
      }

    },
    getResultType(searchResult) {
      switch (searchResult.resulttype) {
        case 'block':
          return 'BlockResult'
        case 'transaction':
          return 'TransactionResult'
      }
    }
  }
}
</script>
