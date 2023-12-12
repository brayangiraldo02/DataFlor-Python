import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Importa Validators y FormGroup

@Component({
  selector: 'app-create-provider',
  templateUrl: './create-provider.component.html',
  styleUrls: ['./create-provider.component.css']
})

export class CreateProviderComponent {
  providerForm: FormGroup; // Define el FormGroup

  constructor(private http: HttpClient, private router: Router, private formBuilder: FormBuilder) {
    this.providerForm = this.formBuilder.group({
      fullname: ['', [Validators.required, Validators.pattern('[a-zA-Z ]*')]],
      address: ['', Validators.required],
      phone: ['', [Validators.required, Validators.pattern('^[0-9]*$')]],
    });
  }

  // Método para enviar los datos al backend y crear un proveedor.
  createProvider() {
    if (this.providerForm.valid) {
      this.http.post('http://localhost:5000/providers/create', this.providerForm.value)
        .subscribe(
          (data: any) => {
            // Manejar respuesta del servidor si es exitosa.
            alert('Proveedor creado exitosamente');
            this.router.navigate(['/providers']);
          },
          (error) => {
            // Manejar error del servidor.
            alert('Error al crear el proveedor');
          }
        );
    } else {
      // Si el formulario no es válido, puedes mostrar un mensaje de error o realizar otras acciones.
      alert('Por favor, complete correctamente el formulario.');
    }
  }
}