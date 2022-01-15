export default class Log {
  static info (value1, value2 = null) {
    if (value2 === null) {
      console.log(value1)
    } else {
      console.log(value1, value2)
    }
  }

  static debug (value1, value2 = null) {
    if (process.env.VUE_APP_DEBUG) {
      if (value2 === null) {
        console.log(value1)
      } else {
        console.log(value1, value2)
      }
    }
  }
}
