import { Component } from '@angular/core';
import { Router } from '@angular/router';
import decoteToken from 'jwt-decode';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent {
  public isLoggedIn: boolean = false;
  public isLoggedInAdmin: boolean = false;
  public isLoggedInOwner: boolean = false;
  public isLoggedInEmployee: boolean = false;
  public showNavbar:boolean = false; //Se crea un bool para el navbar.
  public logo:string = '../../../assets/all/img/dataflor3.png'; //Se crea una variable para el logo.
  public username:string = ''

  constructor (private router: Router) { }

  public logoutPress(): void {
    localStorage.clear();
  }

  //Función para mostrar el navbar responsive.
  public toggleNavbar(): void {
    //Se define valor a mostrar: solo true o false.
    this.showNavbar = !this.showNavbar;
    //Mostrar en consola el valor seleccionado.
    console.log(this.showNavbar);
  }

  ngOnInit(): void {
    const token:any = localStorage.getItem('token');
    const tokenDesencripted:any = decoteToken(token);

    if (tokenDesencripted) {
      this.isLoggedIn = true;
      this.username = tokenDesencripted.user.username;
      if (tokenDesencripted.user.role === 'Admin') {
        this.isLoggedInAdmin = true;
      }
      if (tokenDesencripted.user.role === 'Dueño') {
        this.isLoggedInOwner = true;
      }
      if (tokenDesencripted.user.role === 'Empleado') {
        this.isLoggedInEmployee = true;
      }
    }
  }
}
