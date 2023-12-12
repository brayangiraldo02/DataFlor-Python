import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http'; 


interface User {
  username: string;
  password: string;
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  
  username: string = '';
  password: string = '';
  public logo:string = '../../../assets/all/img/dataflor3.png'; //Se crea una variable para el logo.

  login(): void {

  } 

  constructor (private router: Router, private http: HttpClient) { }

  onSubmit(){
    this.http.post('http://localhost:5000/login', {"username": this.username, "password": this.password}).subscribe((data:any) => {
      console.log(data);
      if (data.token){
        window.alert("Bienvenido");
        localStorage.setItem('token', JSON.stringify(data.token));
        this.router.navigate(['/']);
      }
    }, error => {
      window.alert("Usuario o contraseña incorrectos");
      console.log(error);
    }
    );
  }
}
