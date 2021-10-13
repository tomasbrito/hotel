<template>
  <div class="q-pa-md " align="center">
    <div class="q-gutter-y-md column"  style="max-width: 300px">
      <q-form v-on:submit="reservarFB" >
        <q-select  v-model="tipo"  :options="options" label="Elegir habitacion" lazy-rules :rules="[ val => val != null  || 'Ingrese el tipo de habitacion']"
         />

         <q-input  filled v-model="fechaEntrada" label="Fecha de entrada" mask="date"
            :rules="[ val => val >= this.fechaHoy() || 'Ingrese una fecha valida']">
           <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                  <q-date v-model="fechaEntrada" @input="() => $refs.qDateProxy.hide()" />
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
       <q-input filled v-model="fechaSalida" label="Fecha de salida" mask="date"
        :rules="[val => val > this.fechaEntrada   || 'Ingrese una fecha valida']">
          <template v-slot:append>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                <q-date v-model="fechaSalida" @input="() => $refs.qDateProxy.hide()" />
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
        <q-btn label="Reservar" type="submit" color="primary"/>
       </q-form>
       <div v-if="correcto">
                <q-banner id="banner"  inline-actions class="text-white bg-primary">
                 Se reservo correctamente
                </q-banner>
              </div>
    </div>
  </div>
</template>
<script>
import moment from 'moment'
import { db } from 'boot/firebase'
export default {
  name: 'Reservar',
  data () {
    return {
      correcto: false,
      fechaEntrada: this.fechaHoy(),
      fechaSalida: this.fechaHoy(),
      dense: false,
      options: [
        'Basic', 'Medium', 'Suite'
      ],
      tipo: null
    }
  },
  methods: {
    async reservarFB () {
      try {
        await db.collection('reservas').add({
          idUsuario: this.$store.state.example.idUserlogged,
          fechaEntrada: this.fechaEntrada,
          fechaSalida: this.fechaSalida,
          tipoHabitacion: this.tipo
        })
      } finally {
        this.correcto = true
      }
    },
    fechaHoy: function () {
      return moment().format('YYYY/MM/DD')
    }
  }
}
</script>
