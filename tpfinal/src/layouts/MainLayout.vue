<template>
  <q-layout view="hhh lpR fff">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://i.imgur.com/KkFZ2jU.png">
          </q-avatar>
          Hotel Yatay

        </q-toolbar-title>
            <div v-if="admin" > <q-btn color="primary" label="Admin" q-route-tab to="/admin"  /> </div>
            <div v-if="loguin" >
            <div>
            <q-btn :label="username"  color="primary" @click="medium = true"></q-btn>
                          <q-dialog
                    v-model="medium"
                  >
                    <q-card style="width: 700px; max-width: 80vw;">
                      <q-card-section>
                        <div class="text-h6">Cerrar sesión</div>
                      </q-card-section>

                      <q-card-section class="q-pt-none">
                        ¿Quiere cerrar la sesión?
                      </q-card-section>

                            <q-card-actions align="right" class="bg-white text-teal">
                              <q-btn flat label="OK" @click="logout"></q-btn>
                              <q-btn flat label="Cancelar" v-close-popup></q-btn>
                            </q-card-actions>
                          </q-card>
                        </q-dialog>
          </div>
            </div>
          <div v-else>
            <q-btn color="primary" label="Iniciar sesión" q-route-tab to="/login"  />
          </div>
      </q-toolbar>

      <q-tabs align="center">
        <q-route-tab to="/" label="Habitaciones" />
        <q-route-tab to="/reservar" label="Reservar" />
      </q-tabs>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title class="text-center">
          <q-avatar class="q-pt-xs">
            <img src="https://i.imgur.com/KkFZ2jU.png">
          </q-avatar>
          <div class="h6">Hotel Yatay</div>
          <h6 class="footerText q-ma-none" style="font-size:12px">Yatay 240, CABA, Argentina</h6>
          <h6 class="footerText q-ma-none q-pb-sm" style="font-size:12px">Tel. 4958-9000 </h6>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
export default {
  data () {
    return {
      sizes: ['lg'],
      medium: false
    }
  },
  methods: {
    logout: function () {
      // buscar en el serv
      this.$store.commit('example/login', {
        username: ''
      })
      this.$router.push('/')
    }
  },
  computed: {
    loguin: function () {
      return this.$store.getters['example/loggedIn']
    },
    admin: function () {
      return this.$store.getters['example/isAdmin']
    },
    username: function () {
      return 'Cerrar sesión'
    }
  }
}
</script>

<style lang="sass" scoped>

</style>
