<template>
<div>
<q-btn color="primary" @click="logout" label="Logout" />
</div>
</template>

<script>
export default {
  name: 'Profile',
  beforeCreate: function () {
    if (!this.$store.getters['example/isLogged']) {
      this.$router.push('/login')
    }
  }
}
</script>
