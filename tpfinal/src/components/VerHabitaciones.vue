<template >
  <div class="q-pa-md ">
    <div class="row">
      <!-- Columna fotos -->
        <div class="col-6" style="height: 450px" >
          <div class="col">
            <!-- Carrusel -->
              <div class="q-pa-md " align="text">
                <q-carousel
                  animated
                  v-model="slide"
                  arrows
                  navigation
                  infinite
                  control-color="primary"
                >
                  <q-carousel-slide :name="1" img-src="https://i.imgur.com/vdpVQut.jpg" />
                  <q-carousel-slide :name="2" img-src="https://i.imgur.com/JIUnnd5.jpg" />
                  <q-carousel-slide :name="3" img-src="https://i.imgur.com/zcRHai7.jpg" />
                  <q-carousel-slide :name="4" img-src="https://i.imgur.com/m1ihkOs.jpg" />
                </q-carousel>
              </div>
          </div>
        </div>
         <!-- Columna data -->
        <div class="col-6 " style="height: 450px">
          <h3 class="flex flex-center q-ma-md">Standar</h3>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
          <h3 class="flex flex-center q-ma-md">Precio por noche</h3>
        </div>
    </div>
    <div class="row">
      <!-- Columna data -->
      <div class="col-6 " style="height: 450px">
          <h3 class="flex flex-center q-ma-md">Standar</h3>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
          <h3 class="flex flex-center q-ma-md">Precio por noche</h3>
        </div>
        <div class="col-6 " style="height: 450px">
          <div class="col">
            <!-- Carrusel -->
              <div class="q-pa-md " align="text">
                <q-carousel
                  animated
                  v-model="slide2"
                  arrows
                  navigation
                  infinite
                  control-color="primary"
                >
                  <q-carousel-slide :name="1" img-src="https://i.imgur.com/vdpVQut.jpg" />
                  <q-carousel-slide :name="2" img-src="https://i.imgur.com/JIUnnd5.jpg" />
                  <q-carousel-slide :name="3" img-src="https://i.imgur.com/zcRHai7.jpg" />
                  <q-carousel-slide :name="4" img-src="https://i.imgur.com/m1ihkOs.jpg" />
                </q-carousel>
              </div>
          </div>
        </div>
    </div>
    <div class="row">
       <!-- Columna fotos -->
        <div class="col-6 " style="height: 450px">
          <div class="col">
            <!-- Carrusel -->
              <div class="q-pa-md " align="text">
                <q-carousel
                  animated
                  v-model="slide3"
                  arrows
                  navigation
                  infinite
                  control-color="primary"
                >
                  <q-carousel-slide :name="1" img-src="https://i.imgur.com/vdpVQut.jpg" />
                  <q-carousel-slide :name="2" img-src="https://i.imgur.com/JIUnnd5.jpg" />
                  <q-carousel-slide :name="3" img-src="https://i.imgur.com/zcRHai7.jpg" />
                  <q-carousel-slide :name="4" img-src="https://i.imgur.com/m1ihkOs.jpg" />
                </q-carousel>
              </div>
          </div>
        </div>
        <!-- Columna data -->
        <div class="col-6 " style="height: 450px">
          <h3 class="flex flex-center q-ma-md">Standar</h3>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
              <h5 class="flex flex-center q-ma-md">-Data</h5>
          <h3 class="flex flex-center q-ma-md">Precio por noche</h3>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VerHabitaciones',
  data () {
    return {
      slide: 1,
      slide2: 1,
      slide3: 1
    }
  }
}
</script>

<style lang="sass" scoped>

h2
  margin-top: 10px

.data
  margin: 20px 0px

.row > div
  padding: 10px 15px
  background: rgba(86,61,124,.15)
  border: 1px solid rgba(86,61,124,.2)
.row + .row
  margin-top: 1rem

</style>
