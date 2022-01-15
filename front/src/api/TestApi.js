import axios from 'axios'

export default class TestApi {
  static get () {
    const url = '/'
    return axios.get(url, {
      params: {}
    })
  }
}