import { Component } from '@angular/core'; //Se importa el component para poder usar la notacion @component y decorar una clase de ts

//Se crea una interfaz para los desarrolladores
interface Developer {
  name: string;//Se crea un atributo nombre
  github: string;//Se crea un atributo github
}

//Se crea un arreglo de desarrolladores
const developers: Developer[] = [//Se crea un arreglo de tipo Developer
{name:"Brayan Cataño Giraldo", github:"https://github.com/brayangiraldo02"}
]

//Se crea el componente
@Component({//Se crea el decorador
  selector: 'app-footer',//Se crea el selector
  templateUrl: './footer.component.html',//Se crea el template
  styleUrls: ['./footer.component.css']//Se crea el style
})

//Se exporta la clase
export class FooterComponent {//Se crea la clase
  developers: Developer[] = developers;//Se crea un atributo de tipo Developer
  currentYear: number = 2023//Se crea un atributo de tipo number
}
