<template>
  <q-page >
      <h3 align="center">Habitaciones</h3>
      <VerHabitaciones></VerHabitaciones>
  </q-page>
</template>

<script>
import VerHabitaciones from '../components/VerHabitaciones'
export default {
  name: 'Habitaciones',
  data: function () {
    return {
      nombre: '',
      cantidad: 0
    }
  },
  components: {
    VerHabitaciones
  }
}
</script>
