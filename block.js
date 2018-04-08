//var shajs = require('sha.js')
var sha256 = require('crypto-js/sha256')
//var CryptoJS = require('crypto-js')

//console.log(shajs('sha256').update('42').digest('hex'))
// => 73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049

//console.log(new shajs.sha256().update('42').digest('hex'))
// => 73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049

//var ciphertext = CryptoJS.AES.encrypt('FUCK YEAH', 'lucas123')
// encrypt
//console.log('cypher: ', ciphertext)

//var bytes = CryptoJS.AES.decrypt(ciphertext.toString(), 'lucas123')
//let plaintext = bytes.toString(CryptoJS.enc.Utf8)
//console.log(plaintext)



//console.log(CryptoJS.HmacSHA1("message", "value"))
// console.log(sha256("mensgem"))
class Block {
  constructor(index = 0, previousHash = null,
      data = 'Genesis BLOCK! oi eu sou o goku, hello blockchain', difficult = 1) {
    this.index = index
    this.previousHash = previousHash
    this.data = data
    this.difficult = difficult
    this.timestamp = new Date()
    this.hash = this.generateHash()
    this.nonce = 0

    this.mine
  }
  generateHash () {
    return sha256(this.index, this.previousHash, JSON.stringify(this.data),
      this.timestamp, this.nonce).toString()
  }
  mine () {
    this.hash = this.generateHash()

    while (!(/^0*$/.test(this.hash.substring(0, this.difficult)))) {
      this.nonce ++
      this.hash = this.generateHash()
    }
  }
}

module.exports = Block
