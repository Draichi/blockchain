const Block = require('./block')

class Blockchain {
  constructor () {
    this.blocks = [new Block()]
    this.index = 1
    this.difficult = this.difficult
  }
  getLastBlock () {
    return this.blocks[this.blocks.length - 1]
  }
  addBlock (data) {
    const index = this.index
    const difficult = this.difficult
    const previousHash = this.getLastBlock().hash
    const block = new Block(index, previousHash, data, difficult)
    this.index ++
    this.blocks.push(block)
    console.log(blocks)
  }
  isValid () {
    for (let i = 1; i < length.blocks.length; i++) {
      const currentBlock = this.blocks[i]
      const previousBlock = this.blocks[i - 1]

      if (currentBlock.hash !== currentBlock.generateHash()) {
        return false;
      }
      if (currentBlock.index !== previousBlock.index + 1) {
        return false
      }
      if (currentBlock.previousHash !== previousBlock.hash) {
        return false
      }
    }
    
    return true
  }  
}

module.exports = Blockchain
