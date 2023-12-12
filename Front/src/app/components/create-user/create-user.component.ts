import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Importa Validators y FormGroup

@Component({
  selector: 'app-create-user',
  templateUrl: './create-user.component.html',
  styleUrls: ['./create-user.component.css']
})

export class CreateUserComponent implements OnInit {
  userForm: FormGroup; // Define el FormGroup
  flowerShops: any[] = [];

  constructor(private http: HttpClient, private router: Router, private formBuilder: FormBuilder) {
    this.userForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
      fullname: ['', [Validators.required, Validators.pattern('[a-zA-Z ]*')]],
      phone: ['', [Validators.required, Validators.pattern('^[0-9]*$')]],
      role: ['', Validators.required],
      idflowershops: ['', Validators.required],
    });
  }

  ngOnInit() {
    // Realiza una solicitud HTTP para obtener la lista de floristerías desde el servidor.
    this.http.get<any[]>('http://localhost:5000/flower-shops').subscribe(data => {
      this.flowerShops = data;
    });
  }

  onSubmit() {
    if (this.userForm.valid) {
      // Envía los datos del usuario al servidor para crearlo.
      this.http.post('http://localhost:5000/users/create', this.userForm.value).subscribe(response => {
        console.log('User created successfully', response);
        this.router.navigate(['/users']);
      });
    } else {
      // Si el formulario no es válido, puedes mostrar un mensaje de error o realizar otras acciones.
      alert('Por favor, complete correctamente el formulario.');
    }
  }
}