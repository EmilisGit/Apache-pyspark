Nagrinėsime duomenis, aprašančius siuntų pristatymo bei logistikos įmonės veiklą. Duotajame faile pateikti dalinai struktūrizuoti duomenys apie siuntų išvežiotojų sustojimus, kurie gali būti apibūdinami šias parametrais: 

"marsrutas", "sustojimo data", "sandelio id", "Firma", "Marsruto tipas", "Masinos tipas", "sustojimo tipas", "sustojimo savaites diena", "laikas", "Sustojimo numeris", "siuntu skaicius", "svoris", "svorio grupe", "geografine zona", "pasto kodas", "Aptarnavimo grupe", "tipas", "Laikas iki sustojimo", "Laikas po sustojimo", "Uzkrovimo tipas", "Ar reikalingos paletes", "Laukia", "Sustojimo klientu skaicius", "sustojimo klientu sarasas", "kaina procentas", "kaina vienetais".

Naudodami Apache Spark RDD API atlikite šias užduotis:

    Slenkstinis lygmuo (5-6): Suskaičiuokite mažiausią, didžiausią ir vidutinį (aritmetinis vidurkis) siuntų svorį (laukas "svoris") skirtingose svorio grupėse (laukas "svorio grupe").
    Tipinis lygmuo (7-8): Raskite maršrutus, kurie aplanko daugiau nei vieną geografinę zoną (laukas "geografine zona"). Koks tai procentas nuo visų maršrutų? Raskite atvejus, kai tai daroma ta pačia diena (laukas "sustojimo data"). Koks tai procentas?
    Puikus lygmuo (9-10): Sudarykite lentelę, kurioje matytųsi kiek pristatyta siuntų ("siuntu skaicius") bei aptarnauta klientų ("Sustojimo klientu skaicius") skirtinguose geografinėse zonose ("geografine zona") skirtingomis savaitės dienomis ("sustojimo savaites diena"). Palyginkite užduoties sprendimo laiką su MapReduce versiją.


Kad paleisti jupyter notebook, naudoti: docker compose up