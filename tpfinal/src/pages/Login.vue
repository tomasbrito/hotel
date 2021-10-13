<template>

  <div class="q-pa-md ">

      <div class="row">
        <div class="col">
        </div>
        <div class="col">
          <h6>Inicia sesión para continuar</h6>
          <h6>Mail: admin@admin.com Pw: admin1 para ver menu de administrador </h6>
              <q-form
              v-on:submit="loginFb()"
              >
              <q-input
                filled
                v-model="email"
                label="Email"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Ingrese su nombre de email']"
              />
              <q-input
                filled
                type="password"
                v-model="password"
                label="Contraseña"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Ingrese su contraseña']"
              />
              <div v-if="incorrectos">
                <q-banner id="banner" inline-actions class="text-white bg-red">
                  Los datos ingresados son incorrectos
                </q-banner>
              </div>
              <div>
                <q-btn label="Ingresar" type="submit" color="primary"/>
                <q-btn label="Registrarse" class="q-ml-md" to="/registrarse" color="primary"/>
                <q-btn label="Cancelar" to="/"  color="primary" flat class="q-ml-md" />
              </div>
                </q-form>
        </div>
        <div class="col">
        </div>
      </div>
  </div>
</template>

<script>
import firebase from 'firebase'
import { db } from 'boot/firebase'

export default {
  name: 'Login',
  data: function () {
    return {
      email: '',
      password: '',
      incorrectos: false,
      idUserlogged: ''
    }
  },
  methods: {
    async loginFb () {
      console.log('login')
      firebase.auth().signInWithEmailAndPassword(this.email, this.password)
      try {
        await db.collection('usuarios').where('email', '==', this.email).get()
          .then(data => {
            data.forEach(element => {
              this.idUserlogged = element.id
            })
          })
      } catch (error) {
        console.log(error)
      }
      this.$store.commit('example/login', {
        loggedIn: true,
        email: this.email,
        idUserlogged: this.idUserlogged
      })
      this.$router.push('/')
        .catch(err => {
          this.error = err.message
        })
    }
  }
}
</script>

<style scoped>
#banner{
  margin-bottom: 30px
}
</style>
