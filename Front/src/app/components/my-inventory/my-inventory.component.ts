import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import decoteToken from 'jwt-decode';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-my-inventory',
  templateUrl: './my-inventory.component.html',
  styleUrls: ['./my-inventory.component.css']
})
export class MyInventoryComponent implements OnInit {
  inventoryForm!: FormGroup;
  inventorys: any[] = [];
  providers: any[] = [];
  editingInventory: any;

  public isLoggedInOwner: boolean = false;

  constructor(private http: HttpClient, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.getInventory();

    this.http.get<any[]>('http://localhost:5000/providers').subscribe((data: any[]) => {
      this.providers = data;
    });

    const token: any = localStorage.getItem('token');
    const tokenDesencripted: any = decoteToken(token);

    if (tokenDesencripted) {
      if (tokenDesencripted.user.role === 'Dueño') {
        this.isLoggedInOwner = true;
      }
    }
  }

  editInventory(inventory: any) {
    this.http.get<any[]>('http://localhost:5000/providers').subscribe((data: any[]) => {
      this.providers = data;
      this.editingInventory = { ...inventory };
      this.inventoryForm = this.formBuilder.group({
        quantity: [this.editingInventory.quantity, [Validators.required, Validators.pattern('^[0-9]*$')]],
        providerid: [this.editingInventory.providerid, Validators.required],
        state: [this.editingInventory.state, Validators.required],
      });
    });
  }
  

  updateInventory() {
    if (this.editingInventory && this.inventoryForm.valid) {
      this.editingInventory = { ...this.editingInventory, ...this.inventoryForm.value };
      this.http.put(`http://localhost:5000/inventory/update/id/${this.editingInventory.inventoryid}`, this.editingInventory)
        .subscribe((response: any) => {
          if (response.message === "Inventory updated successfully") {
            const index = this.inventorys.findIndex(inventory => inventory.inventoryid === this.editingInventory.inventoryid);
            this.inventorys[index] = { ...this.editingInventory };
            this.editingInventory = null;
            this.inventoryForm.reset();
            window.location.reload();
          }
        });
    }
  }

  cancelEdit() {
    this.editingInventory = null;
    this.inventoryForm.reset();
  }

  getInventory() {
    this.http.get('http://localhost:5000/inventory')
      .subscribe((data: any) => {
        this.inventorys = data.sort((a: any, b: any) => b.state - a.state);
      });
  }
}
