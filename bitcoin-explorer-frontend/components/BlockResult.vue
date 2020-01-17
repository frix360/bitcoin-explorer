<template>
  <v-card>
    <v-card-title>Block found:</v-card-title>
    <v-card-text>
      <v-row>
        <v-col>
          <v-card outlined>
            <v-card-title>
              General info:
            </v-card-title>
            <v-card-text>
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Hash:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.hash}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Height:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.height}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Time:</v-list-item-title>
                    <v-list-item-subtitle>{{unixTimeToDateTime(resultData.time)}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Previous block hash:</v-list-item-title>
                    <v-list-item-subtitle style="cursor: pointer" @click="handleHashClick(resultData.previousblockhash)">{{resultData.previousblockhash}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Transactions count:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.tx.length}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Difficulty:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.difficulty}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Confirmations:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.confirmations}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Nonce:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.nonce}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Size:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.size}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Version:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.version}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-card outlined>
            <v-card-title>First 50 transactions:</v-card-title>
            <v-card-text>
              <v-list>
                <v-list-item v-for="txid in resultData.tx.slice(0, 50)" @click="(e) => handleHashClick(txid)">{{txid}}</v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import moment from 'moment'
export default {
  name: 'BlockResult',
  props: {
    resultData: {
      type: Object,
      default: () => ({})
    }
  },
  methods: {
    unixTimeToDateTime(value) {
      return moment.unix(value).format("YYYY/MM/DD HH:mm:ss");
    },

    handleHashClick(hash) {
      this.$emit('hashClicked', hash)
    }
  }
}
</script>

<style scoped></style>
