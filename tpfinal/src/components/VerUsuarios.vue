<template>
  <div class="q-pa-md">
    <q-table
      title="Usuarios"
      :data="data"
      :columns="columns"
      selection="single"
      :selected.sync="selected"
    />
  </div>
</template>

<script>
import { db } from 'boot/firebase'

export default {
  name: 'verUsuarios',
  beforeCreate: function () {
    if (!this.$store.getters['example/isAdmin']) {
      this.$router.push('/')
    }
  },
  created: function () {
    this.buscarUsuarios()
  },
  data: function () {
    return {
      name: 'juan',
      selected: [],
      data: [],
      usuario: {},
      columns: [
        { name: 'usuario', required: true, label: 'Usuario', align: 'left', field: 'nombre', format: val => `${val}`, sortable: true },
        { name: 'ID', align: 'center', label: 'ID', field: 'idUsuario', sortable: true },
        { name: 'email', align: 'center', label: 'Email', field: 'email', sortable: true },
        { name: 'celular', align: 'center', label: 'Celular', field: 'celular', sortable: true }
      ]
    }
  },
  methods: {
    async buscarUsuarios () {
      try {
        const query = await db.collection('usuarios').get()
        query.forEach(element => {
          const usuario = { email: element.data().email, celular: element.data().celular, idUsuario: element.id, nombre: element.data().nombre }
          this.data.push(usuario)
        })
      } catch (error) {
        console.log(error)
      } finally {
        console.log('busqueda ok')
      }
    }
  }
}
</script>
