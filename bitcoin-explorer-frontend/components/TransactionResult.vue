<template>
  <v-card>
    <v-card-title>Transaction found</v-card-title>
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
                    <v-list-item-title>Txid:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.txid}}</v-list-item-subtitle>
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
                    <v-list-item-title>Hash:</v-list-item-title>
                    <v-list-item-subtitle>{{resultData.hash}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Block hash::</v-list-item-title>
                    <v-list-item-subtitle style="cursor: pointer" @click="handleHashClick(resultData.blockhash)">{{resultData.blockhash}}</v-list-item-subtitle>
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
            <v-card-title>Outputs:</v-card-title>
            <v-card-text>
              <v-simple-table>
                <thead>
                <tr>
                  <th>No.</th>
                  <th>Value</th>
                </tr>
                </thead>

                <tbody>
                <tr v-for="output in resultData.vout">
                  <td>{{output.n}}</td>
                  <td>{{output.value}}</td>
                </tr>
                </tbody>
              </v-simple-table>
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
  name: 'TransactionResult',
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
