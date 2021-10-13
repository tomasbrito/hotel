<template>
  <div class="q-pa-md">
    <q-table
      title="Reservas"
      :data="data"
      :columns="columns"
      selection="single"
      :selected.sync="selected"
    />
     <q-btn label="Eliminar reserva"  class=" q-mt-md" v-on:click="borrarReserva" color="primary"/>
      <div v-if="this.userReserva != ''">
        <q-btn label="Ver datos del usuario" color="primary" class=" q-mt-md" @click="medium = true"></q-btn>

        <!--Dialog para mostrar los datos del usuario dueño de la reserva-->
        <q-dialog v-model="medium">
          <q-card style="width: 700px; max-width: 80vw;">
            <q-card-section>
              <div class="text-h6">Datos</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
             Nombre de usuario: {{this.userReserva.nombre}}
            </q-card-section>
            <q-card-section class="q-pt-none">
             ID: {{this.userReserva.idUsuario}}
            </q-card-section>
            <q-card-section class="q-pt-none">
             Email: {{this.userReserva.email}}
            </q-card-section>
            <q-card-section class="q-pt-none">
             Celular: {{this.userReserva.celular}}
            </q-card-section>

            <q-card-actions align="right" class="bg-white text-teal">
              <q-btn flat label="Cancelar" v-close-popup></q-btn>
            </q-card-actions>
          </q-card>
        </q-dialog>
      </div>
  </div>
</template>

<script>
import { db } from 'boot/firebase'
export default {
  name: 'verReservas',
  beforeCreate: function () {
    if (!this.$store.getters['example/isAdmin']) {
      this.$router.push('/')
    }
  },
  created: function () {
    this.buscarReservas()
  },
  data: function () {
    return {
      userReserva: '',
      medium: false,
      selected: [],
      data: [],
      columns: [
        { name: 'Habitacion', required: true, label: 'Habitacion', align: 'left', field: 'tipoHabitacion', format: val => `${val}`, sortable: true },
        { name: 'entrada', align: 'center', label: 'Fecha de entrada', field: 'fechaEntrada', sortable: true },
        { name: 'salida', align: 'center', label: 'Fecha de salida', field: 'fechaSalida', sortable: true },
        { name: 'ID', align: 'center', label: 'Id', field: 'id', sortable: true },
        { name: 'IdUsuario', align: 'center', label: 'ID de usuario', field: 'idUsuario', sortable: true }
      ]
    }
  },
  watch: {
    selected: function () {
      this.buscarUsuario()
    }
  },
  methods: {
    async buscarReservas () {
      try {
        const query = await db.collection('reservas').get()
        query.forEach(element => {
          const reserva = { id: element.id, fechaEntrada: element.data().fechaEntrada, fechaSalida: element.data().fechaSalida, idUsuario: element.data().idUsuario, tipoHabitacion: element.data().tipoHabitacion }
          this.data.push(reserva)
        })
      } catch (error) {
        console.log(error)
      }
    },
    async borrarReserva () {
      const id = this.selected[0].id
      await db.collection('reservas').doc(id).delete()
        .then(() => {
          this.data = []
          this.buscarReservas()
        })
    },
    async buscarUsuario () {
      const id = this.selected[0].idUsuario
      try {
        const query = await db.collection('usuarios').doc(id).get()
        this.userReserva = query.data()
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>
