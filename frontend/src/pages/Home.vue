<template>
  <div>
    <b-container :fluid="true">
      <b-row align-v="baseline">
        <b-col>
          <H1 class="title">Search for a Redfin Property</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="1" :max="6" :label="'Progress: 1/6'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>

      <b-row align-v="start">
        <b-col sm="6">
          <TextInput class="mb-0 pb-0" v-model="queryUrl" text-label="Type property address..."></TextInput>
          <p class="mt-0 pt-0 text-muted font-weight-lighter font-weight-italic redfinURL">{{ pdfBody.url }}</p>
        </b-col>
        <b-col sm="6">
          <b-button block variant="outline-success" :disabled="!pdfBody.url" @click="nextPage">Next Page <arrow-right-circle /></b-button>
        </b-col>
      </b-row>

      <b-row align-v="baseline">
        <b-col sm="6">
          <b-list-group class="py-sm-1 cursor-selectable" v-for="(property, index) in propertiesList"
                        :key="property.id">
            <b-list-group-item class="mt-1" v-bind:class="{ 'active' : isSelected(index)}" @click="saveUrl(index)">
              {{ property.name }} {{ property.subName }}
            </b-list-group-item>
          </b-list-group>
        </b-col>
      </b-row>

    </b-container>
  </div>
</template>

<script>
import * as axios from 'axios'
import PdfBody from '../models/PdfBody.js'
import TextInput from '../components/TextInput'
import CheckboxInput from '../components/CheckboxInput'
import ArrowRightCircle from '../components/icons/ArrowRightCircle'

export default {
  name: 'Home',
  components: {
    CheckboxInput,
    TextInput,
    ArrowRightCircle
  },
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  data () {
    return {
      selected: null,
      pdfBody: new PdfBody(),
      redfinUrl: '',
      pdfName: '',
      queryUrl: null,
      fruits: ['apple', 'banana', 'orange'],
      propertiesList: []
    }
  },
  mounted () {
    this.searchRedfinUrl()
    localStorage.pdfBody = new PdfBody()
  },
  watch: {
    queryUrl: function () {
      this.searchRedfinUrl()
    }
  },
  methods: {
    isSelected (i) {
      return i === this.selected
    },
    searchRedfinUrl () {
      this.propertiesList = []
      if (this.queryUrl) {
        axios({
          url: 'http://50.116.19.93:8000/api/search/',
          method: 'POST',
          data: {url: 'https://www.redfin.com/stingray/do/location-autocomplete?location=' + this.queryUrl + '&count=10&v=2'}
        }).then(response => {
          if (response.data) {
            response.data.properties.forEach(property => this.propertiesList.push(property))
          }
        })
      }
    },
    saveUrl (index) {
      this.pdfBody.url = 'https://www.redfin.com' + this.propertiesList[index].url
      this.selected = index
    },
    nextPage () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'ConfirmPropertyDetails'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cursor-selectable {
  cursor: pointer;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
.redfinURL {
  font-size: 0.7em;
}
</style>
