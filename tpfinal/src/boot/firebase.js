import firebase from 'firebase/app'
import 'firebase/firestore'

const firebaseConfig = {
  apiKey: 'AIzaSyDqeUVa0yg9WgJFEDvS5sozvkjc9EDX5aU',
  authDomain: 'hotel-a0c92.firebaseapp.com',
  projectId: 'hotel-a0c92',
  storageBucket: 'hotel-a0c92.appspot.com',
  messagingSenderId: '550132242235',
  appId: '1:550132242235:web:14c0e997820c49ed0a891e'
}

const firebaseApp = firebase.initializeApp(firebaseConfig)
const db = firebase.firestore()

export { db, firebase, firebaseApp }
