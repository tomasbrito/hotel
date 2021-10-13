<template>
<div class="q-pa-md ">
      <div class="row">
        <div class="col">
        </div>
        <div class="col">
          <h6>Inicia sesión para continuar</h6>
              <q-form  v-on:submit="register()">
        <q-input
           filled
          v-model="username"
          label="Usuario"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Ingrese su nombre de usuario']"
          class="q-l-lg"
        />
        <q-input
          filled
          type="password"
          v-model="password"
          label="Contraseña"
          lazy-rules
          :rules="[ val => val && val.length > 5 || 'La contraseña debe tener mas de 5 caracteres']"
        />
        <q-input
          filled
          type="password"
          v-model="confirmPassword"
          label="Confirme su contraseña"
          lazy-rules
          :rules="[ val => val == password || 'Las contraseñas no coinciden']"
        />
        <q-input
          filled
          type="email"
          v-model="email"
          label="Email"
          lazy-rules
          :rules="[ val => val.length > 0 || 'Ingrese su email']"
        />
        <q-input
          filled
          type="celular"
          v-model="celular"
          label="Celular"
          lazy-rules
          :rules="[ val => val.length > 0 || 'Ingrese su celular']"
        />
        <div v-if="incorrectos">
                <q-banner id="banner"  inline-actions class="text-white bg-red q-ma-md">
                  Nombre de usuario ya utilizado
                </q-banner>
              </div>
        <div>
          <q-btn label="Registrarse" type="submit" color="primary"/>
          <q-btn label="Cancelar" class="q-ml-md" to='/login' flat color="primary"/>
        </div>
      </q-form>
        </div>
        <div class="col">
        </div>
      </div>
  </div>
  </template>

<script>

import axios from 'axios'
import firebase from 'firebase'
import { db } from 'boot/firebase'

export default {
  name: 'Registrarse',
  data: function () {
    return {
      email: '',
      username: '',
      password: '',
      confirmPassword: '',
      celular: '',
      incorrectos: false
    }
  },
  methods: {
    registrarse: function () {
      const formData = new FormData()
      formData.set('username', this.username)
      formData.set('password', this.password)
      formData.set('celular', this.celular)
      formData.set('email', this.email)
      axios.post('http://127.0.0.1:9001/registrar', formData)
        .then((response) => {
          this.$router.push('/login')
        }).catch((error) => {
          this.incorrectos = true
          console.log(error)
        })
    },
    async register () {
      firebase.auth().createUserWithEmailAndPassword(this.email, this.password)
      try {
        await db.collection('usuarios').add({
          email: this.email,
          nombre: this.username,
          celular: this.celular
        })
      } finally {
        this.correcto = true
      }
      this.$router.push('/login')
    }
  }
}
</script>
