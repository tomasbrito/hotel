<template>
  <q-page>
      <h3 align="center">Reservar</h3>
      <reservar></reservar>

  </q-page>
</template>

<script>
import Reservar from '../components/reservar'
export default {
  name: 'Reserva',
  beforeCreate: function () {
    if (!this.$store.getters['example/loggedIn']) {
      this.$router.push('/login')
    }
  },
  data: function () {
    return {
      nombre: '',
      cantidad: 0
    }
  },
  components: {
    Reservar
  }
}
</script>
