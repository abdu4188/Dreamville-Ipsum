import { getParagraphs, getSentences, getWords } from './utils'

export const getLyrics = (type, value, artist) => {
  if (type === 'words') {
    const words = getWords(Number(value), artist)
    return words
  } else if (type === 'sentences') {
    const sentences = getSentences(Number(value), artist)
    return sentences
  } else if (type === 'paragraphs') {
    const paragraphs = getParagraphs(Number(value), artist)
    return paragraphs
  }
}
