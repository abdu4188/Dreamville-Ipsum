import songs from './songs.json'

export const getParagraphs = (n, artist) => {
  const paragraphs = []
  do {
    const sentences = getSentences(getRandomNumber(), artist)
    paragraphs.push(sentences)
  } while (paragraphs.length < n)
  return paragraphs.join('\n')
}

export const getRandomItem = (array) => {
  return array[Math.floor(Math.random() * array.length)]
}

export const getRandomNumber = (min = 3, max = 7) => {
  return Math.random() * (max - min) + min
}

export const getSentences = (n, artist) => {
  const filteredSongs = songs.filter(
    (song) => {
      return song.artist === artist
    })
  const sentences = []
  do {
    const song = getRandomItem(filteredSongs)
    const sentence = getRandomItem(song.lyrics)
    sentences.push(sentence)
  } while (sentences.length < n)
  return sentences.join('. ') + '.'
}

export const getWords = (n, artist) => {
  const filteredSongs = songs.filter(
    (song) => {
      return song.artist === artist
    })
  let words
  do {
    const song = getRandomItem(filteredSongs)
    words = getRandomItem(song.lyrics)
  } while (words.split(' ').length !== n)
  return words + '.'
}
