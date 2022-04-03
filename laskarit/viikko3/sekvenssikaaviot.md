## Tehtävä 3
```mermaid
sequenceDiagram
  main->>machine: Machine()
  
  machine->>tank: FuelTank()
  machine->>tank: fill(40)
  machine->>engine: Engine(tank)
  
  
  main->>machine: drive()
  activate machine
  
  machine->>engine: start()
  activate engine
  engine->>tank: consume(5)
  activate tank
  deactivate tank
  engine-->>machine: 
  deactivate engine
  
  machine->>engine: is_running()
  activate engine
  engine->>tank: asks for fuel_contents
  activate tank
  tank-->>engine: fuel_contents = 35
  deactivate tank
  engine-->>machine: True
  deactivate engine
  
  machine->>engine: use_energy()
  activate engine
  engine->>tank: consume(10)
  activate tank
  deactivate tank
  engine-->>machine: 
  deactivate engine
  machine-->>main: 
  deactivate machine
```

## Tehtävä 4
```mermaid
sequenceDiagram
  main->>laitehallinto: HKLLaitehallinto()
  main->>rautatientori: Lataajalaite()
  main->>ratikka6: Lukijalaite()
  main->>bussi244: Lukijalaite()
  
  main->>laitehallinto: lisaa_lataaja(rautatientori)
  main->>laitehallinto: lisaa_lukija(ratikka6)
  main->>laitehallinto: lisaa_lukija(bussi244)
  
  main->>lippuluukku: Kioski()
  main->>lippuluukku: osta_matkakortti("Kalle")
  activate lippuluukku
  lippuluukku-->>kallen_kortti: kallen_kortti
  deactivate lippuluukku
  
  main->>rautatientori: lataa_arvoa(kallen_kortti, 3)
  activate rautatientori
  rautatientori->>kallen_kortti: kasvata_arvoa(3)
  activate kallen_kortti
  deactivate kallen_kortti
  rautatientori-->>main: 
  deactivate rautatientori
  
  main->>ratikka6: osta_lippu(kallen_kortti, 0)
  activate ratikka6
  ratikka6->>kallen_kortti: katso arvo
  activate kallen_kortti
  kallen_kortti-->>ratikka6: 3
  deactivate kallen_kortti
  ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
  activate kallen_kortti
  deactivate kallen_kortti
  ratikka6-->>main: True
  deactivate ratikka6
  
  main->>bussi244: osta_lippu(kallen_kortti, 2)
  activate bussi244
  bussi244->>kallen_kortti: katso arvo
  activate kallen_kortti
  kallen_kortti-->>bussi244: 1.5
  deactivate kallen_kortti
  bussi244-->>main: False
  deactivate bussi244
```
