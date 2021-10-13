export default {
  login: function (state, data) {
    state.loggedIn = data.loggedIn
    state.email = data.email
    state.idUserlogged = data.idUserlogged
  }
}
