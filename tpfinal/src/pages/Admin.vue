<template>
    <div>
        <h5 align=center>Usuarios</h5>
        <verUsuarios></verUsuarios>
        <h5 align=center>Reservas</h5>
        <verReservas></verReservas>

    </div>
</template>

<script>
import verUsuarios from '../components/verUsuarios'
import verReservas from '../components/verReservas'
export default {
  name: 'admin',
  components: {
    verUsuarios,
    verReservas
  }
}
</script>
