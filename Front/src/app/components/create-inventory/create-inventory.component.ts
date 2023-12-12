import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Importa Validators y FormGroup
import decoteToken from 'jwt-decode';

@Component({
  selector: 'app-create-inventory',
  templateUrl: './create-inventory.component.html',
  styleUrls: ['./create-inventory.component.css']
})
export class CreateInventoryComponent {
  inventoryForm: FormGroup; // Define el FormGroup
  idflowershops!: [] 
  products: any[] = [];
  providers: any[] = [];

  constructor(private http: HttpClient, private router: Router, private formBuilder: FormBuilder) {
    this.inventoryForm = this.formBuilder.group({
      productid: ['', Validators.required],
      providerid: ['', Validators.required],
      quantity: ['', [Validators.required, Validators.pattern('^[0-9]*$')]],
    });
  }

  ngOnInit(): void {
    this.http.get<any[]>('http://localhost:5000/products').subscribe(data => {
      this.products = data;
    });
    this.http.get<any[]>('http://localhost:5000/providers').subscribe(data => {
      this.providers = data;
    });

    const token:any = localStorage.getItem('token');
    const tokenDesencripted:any = decoteToken(token);

    this.idflowershops = tokenDesencripted.user.idflowershops;

  }

  // Método para enviar los datos al backend y crear un proveedor.
  createProduct() {
    if (this.inventoryForm.valid) {
      this.inventoryForm.value.idflowershops = this.idflowershops;
      this.http.post('http://localhost:5000/inventory/create', this.inventoryForm.value)
        .subscribe(
          (data: any) => {
            // Manejar respuesta del servidor si es exitosa.
            alert('Producto creado exitosamente');
            this.router.navigate(['/my-inventories']);
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
