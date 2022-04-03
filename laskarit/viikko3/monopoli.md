## Tehtävä 1
```mermaid
classDiagram
  class Noppa
  class Pelaaja{
    pelinappula: Pelinappula
  }
  class Pelilauta {
    ruudut: list
  }
  class Ruutu{
    seuraava: Ruutu
  }
  class Pelinappula {
    sijainti: Ruutu
  }
  Pelaaja "1"--"1" Pelinappula
  Ruutu .. Pelinappula
  Pelilauta "1"--"40" Ruutu
```
