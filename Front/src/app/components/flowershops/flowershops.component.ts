import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Importa Validators y FormGroup

@Component({
  selector: 'app-flowershops',
  templateUrl: './flowershops.component.html',
  styleUrls: ['./flowershops.component.css'] // Agrega el archivo CSS si lo tienes
})

export class FlowershopsComponent implements OnInit {
  flowerShops: any[] = []; // Arreglo para almacenar las floristerías
  selectedFlowerShop: any; // Floristería seleccionada para edición
  isEditing: boolean = false; // Variable para controlar la edición
  flowerShopForm!: FormGroup; // Define el FormGroup

  constructor(private http: HttpClient, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.getFlowerShops();
  }

  // Obtener la lista de floristerías desde el servidor
  getFlowerShops() {
    this.http.get('http://localhost:5000/flower-shops')
      .subscribe((data: any) => {
        this.flowerShops = data.sort((a: any, b: any) => b.state - a.state);
      });
  }

  // Redirigir a la página de inventario (puedes implementarlo más tarde)
  goToInventory(id: number) {
    // Implementa la redirección a la página de inventario
  }

  goToSales(id: number) {
    // Implementa la redirección a la página de ventas
  }

  // Mostrar el formulario de edición para la floristería seleccionada
  editFlowerShop(flowerShop: any) {
    this.selectedFlowerShop = { ...flowerShop };
    this.isEditing = true;

    // Inicializar el formulario con los valores de la floristería seleccionada
    this.flowerShopForm = this.formBuilder.group({
      fullname: [this.selectedFlowerShop.fullname, [Validators.required, Validators.pattern('[a-zA-Z ]*')]],
      address: [this.selectedFlowerShop.address, Validators.required],
      phone: [this.selectedFlowerShop.phone, [Validators.required, Validators.pattern('^[0-9]*$')]],
      state: [this.selectedFlowerShop.state, Validators.required],
    });
  }

  // Guardar los cambios en la floristería
  saveChanges() {
    if (this.selectedFlowerShop && this.flowerShopForm.valid) {
      // Actualizar los valores de la floristería seleccionada con los del formulario
      this.selectedFlowerShop = { ...this.selectedFlowerShop, ...this.flowerShopForm.value };
      
      this.http.put(`http://localhost:5000/flower-shops/update/id/${this.selectedFlowerShop.idflowershops}`, this.selectedFlowerShop)
        .subscribe((data: any) => {
          // Actualizar la lista de floristerías después de la edición
          this.getFlowerShops();
          this.selectedFlowerShop = null;
          this.isEditing = false;
        });
    } else {
      // Si el formulario no es válido, puedes mostrar un mensaje de error o realizar otras acciones.
      window.alert('Por favor, complete correctamente el formulario.');
    }
  }

  // Cancelar la edición y volver a la lista
  cancelEdit() {
    this.selectedFlowerShop = null;
    this.isEditing = false;
  }
}
