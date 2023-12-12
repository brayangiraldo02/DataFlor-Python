import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-inventory',
  templateUrl: './inventory.component.html',
  styleUrls: ['./inventory.component.css']
})
export class InventoryComponent {
  inventorys: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getInventory();
  }

  // Obtener la lista de floristerías desde el servidor
  getInventory() {
    this.http.get('http://localhost:5000/inventory')
      .subscribe((data: any) => {
        this.inventorys = data;
      });
  }

}
