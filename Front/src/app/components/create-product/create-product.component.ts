import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Importa Validators y FormGroup


@Component({
  selector: 'app-create-product',
  templateUrl: './create-product.component.html',
  styleUrls: ['./create-product.component.css']
})
export class CreateProductComponent {
  productForm: FormGroup; // Define el FormGroup

  constructor(private http: HttpClient, private router: Router, private formBuilder: FormBuilder) {
    this.productForm = this.formBuilder.group({
      productname: ['', [Validators.required, Validators.pattern('[a-zA-Z ]*')]],
      price: ['', [Validators.required, Validators.pattern('^[0-9]*$')]],
    });
  }

  // Método para enviar los datos al backend y crear un proveedor.
  createProduct() {
    if (this.productForm.valid) {
      this.http.post('http://localhost:5000/products/create', this.productForm.value)
        .subscribe(
          (data: any) => {
            // Manejar respuesta del servidor si es exitosa.
            alert('Producto creado exitosamente');
            this.router.navigate(['/products']);
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
