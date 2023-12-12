import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Importar Validators y FormGroup

@Component({
  selector: 'app-create-flowershop',
  templateUrl: './create-flowershop.component.html',
  styleUrls: ['./create-flowershop.component.css']
})

export class CreateFlowershopComponent {
  flowerShopForm: FormGroup; // Define el FormGroup

  constructor(private http: HttpClient, private router: Router, private formBuilder: FormBuilder) {
    this.flowerShopForm = this.formBuilder.group({
      fullname: ['', [Validators.required, Validators.pattern('[a-zA-Z ]*')]],
      address: ['', Validators.required],
      phone: ['', [Validators.required, Validators.pattern('^[0-9]*$')]],
    });
  }

  // Método para enviar los datos al backend y crear una floristería.
  createFlowerShop() {
    if (this.flowerShopForm.valid) {
      this.http.post('http://localhost:5000/flower-shops/create', this.flowerShopForm.value)
        .subscribe(
          (data: any) => {
            // Manejar respuesta del servidor si es exitosa.
            alert('Floristería creada exitosamente');
            this.router.navigate(['/flowershops']);
          },
          (error) => {
            // Manejar error del servidor.
            alert('Error al crear la floristería');
          }
        );
    } else {
      // Si el formulario no es válido, puedes mostrar un mensaje de error o realizar otras acciones.
      alert('Por favor, complete correctamente el formulario.');
    }
  }
}