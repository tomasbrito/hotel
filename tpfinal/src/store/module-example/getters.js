export default {
  loggedIn: function (state) {
    return state.loggedIn
  },
  isAdmin: function (state) {
    return (state.email === 'admin@admin.com')
  }
}
