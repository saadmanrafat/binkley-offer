<template>
  <div>
    <b-container :fluid="true">
      <b-row>
        <b-col>
          <H1 class="title">Offer Details</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="4" :max="6" :label="'Progress: 4/6'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
      <HeaderSiteMap :site-map="siteMap"></HeaderSiteMap>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Purchase Price: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInputMoney prepend="$" title="Purchase Price" v-model="pdfBody.purchase_price"
                          text-label="Purchase Price"></TextInputMoney>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Closing Cost Credit: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <RadioInputTwoOptions :special-field="true" text-label="Credit Buyer at Closing: "
                                :item="creditBuyerAtClosingRadioItem" item-one-label=" Yes"
                                item-two-label="No"></RadioInputTwoOptions>
          <TextInputMoney title="Dollar Amount" prepend="$" :special-field="true" text-label="Dollar Amount"
                          v-model="pdfBody.credit_buyer_at_closing_if_yes_amount"></TextInputMoney>
          <b-form-group
            label-cols-sm="3"
            label="or"
            label-align-sm="right">
          </b-form-group>
          <TextInputMoney title="Percent Amount" prepend="%" :special-field="true" text-label="Percent Amount"
                          v-model="pdfBody.credit_buyer_at_closing_if_no_percentage"></TextInputMoney>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Home Warranty: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInputMoney title="Home Warranty Amount" prepend="$" v-model="pdfBody.home_warranty_amount"
                          text-label="Home Warranty Amount"></TextInputMoney>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Earnest Money: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInputMoney title="Brokerage For Earnest Money" prepend="$" v-model="pdfBody.brokerage_for_earnest_money"
                          text-label=" "></TextInputMoney>
          <TextInputMoney title="Earnest Money Payment Type" prepend="$" v-model="pdfBody.initial_earnest_money_amount"
                          text-label=" "></TextInputMoney>
          <TextInput :special-field="true" title="Earnest Money Payment Type"
                     v-model="pdfBody.how_buyer_deposits_earnest_money"
                     text-label=" "></TextInput>
          <TextInput :special-field="true" title="Initial Earnest Money Payment Period"
                     v-model="pdfBody.initial_earnest_money_due_date"
                     text-label=" "></TextInput>
          <TextInputMoney title="Balance of Earnest Money Amount" prepend="$"
                          v-model="pdfBody.balance_of_earnest_money_amount"
                          text-label="Dollar Amount"></TextInputMoney>
          <b-form-group
            label-cols-sm="3"
            label="or"
            label-align-sm="right">
          </b-form-group>
          <TextInputMoney title="Balance of Earnest Money Due Date" prepend="%"
                          v-model="pdfBody.balance_of_earnest_money_due_date"
                          text-label="Percent Amount"></TextInputMoney>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Mortgage Contingency: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <RadioInputTwoOptions :special-field="true" :item="mortgageRadioItem"
                                text-label="Contract Subject to Mortgage: "
                                item-one-label="Yes"
                                item-two-label="No"></RadioInputTwoOptions>
          <TextInputDate title="Mortgage Contingency Date" v-model="pdfBody.mortgage_contingency_date"
                         text-label="Mortgage Contingency Date"></TextInputDate>
          <TextInputMoney title="Buyer Interest Rate" prepend="$" v-model="pdfBody.buyer_interest_rate"
                          text-label=" "></TextInputMoney>
          <TextInput :special-field="true" title="Buyer Loan Term" v-model="pdfBody.buyer_loan_term"
                     text-label=" "></TextInput>
          <TextInputMoney title="Buyer Loan to Value" prepend="%" v-model="pdfBody.buyer_loan_to_value"
                          text-label=" "></TextInputMoney>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-0">
        <b-form-group
          label-cols-lg="3"
          label="Closing: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInputDate title="Closing Date" v-model="pdfBody.closing_date" text-label="Closing Date"></TextInputDate>
        </b-form-group>
      </b-card>
      <b-row>
        <b-col>
          <b-button class="btn float-right mr-auto" variant="primary" @click="nextPage">Next Page</b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import CheckboxInput from '../components/CheckboxInput'
import TextInput from '../components/TextInput'
import TextInputMoney from '../components/TextInputMoney'
import PdfBody from '../models/PdfBody'
import TextInputDate from '../components/TextInputDate'
import RadioInputTwoOptions from '../components/RadioInputTwoOptions'
import HeaderSiteMap from '../components/HeaderSiteMap'

export default {
  name: 'OfferDetails',
  components: {HeaderSiteMap, RadioInputTwoOptions, TextInputDate, CheckboxInput, TextInput, TextInputMoney},
  data () {
    return {
      pdfBody: new PdfBody(),
      mortgageRadioItem: {
        first: false,
        second: false
      },
      creditBuyerAtClosingRadioItem: {
        first: false,
        second: false
      },
      siteMap: [
        {
          displayName: 'Address/',
          pageUrl: 'Home',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Property Details/',
          pageUrl: 'ConfirmPropertyDetails',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Fixtures And Personal Property/',
          pageUrl: 'FixturesAndPersonalProperty',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Offer Details',
          pageUrl: 'OfferDetails',
          isDisabled: true,
          color: 'gray'
        }
      ]
    }
  },
  watch: {
    creditBuyerAtClosingRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.credit_buyer_at_closing_yes = Boolean(this.creditBuyerAtClosingRadioItem.first)
        this.pdfBody.credit_buyer_at_closing_no = Boolean(this.creditBuyerAtClosingRadioItem.second)
      }
    },
    mortgageRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.contract_subject_to_mortgage_yes = Boolean(this.mortgageRadioItem.first)
        this.pdfBody.contract_subject_to_mortgage_no = Boolean(this.mortgageRadioItem.second)
      }
    }
  },
  mounted () {
    if (localStorage.pdfBody) {
      this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
    }
  },
  methods: {
    nextPage () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'LegalMumboJumbo'})
    }
  }
}
</script>

<style scoped>

</style>
