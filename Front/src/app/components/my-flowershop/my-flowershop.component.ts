import { Component } from '@angular/core';
import jwtDecode from 'jwt-decode';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { OnInit } from '@angular/core';

@Component({
  selector: 'app-my-flowershop',
  templateUrl: './my-flowershop.component.html',
  styleUrls: ['./my-flowershop.component.css']
})
export class MyFlowershopComponent implements OnInit{
  flowershopId: any = 0;
  flowershopData: any = {};
  inEditMode: boolean = false;


  enterEditMode() {
    this.inEditMode = true;
  }

  constructor(private router: Router, private http: HttpClient) { }

  ngOnInit(): void {
    this.getOwnerInfo();
    this.getFlowershop();
  }

  getOwnerInfo(){
    const token: any = localStorage.getItem('token');
    const tokenDesencripted: any = jwtDecode(token);
    this.flowershopId = tokenDesencripted.user.idflowershops;
  }

  getFlowershop(): void {
    this.http.get(`http://localhost:5000/flower-shops/${this.flowershopId}`).subscribe((data: any) => {
      this.flowershopData = data;
    }, error => {
      console.log(error);
    }
    );
  }

  navigateTo(route: string) {
    this.router.navigate([route]);
  }

  updateFlowershop(): void {
    this.http.put(`http://localhost:5000/flower-shops/update/id/${this.flowershopId}`, this.flowershopData).subscribe((data: any) => {
      this.flowershopData = data;
      console.log(this.flowershopData);
      window.alert("Flower shop updated successfully");
      this.getFlowershop();
      this.inEditMode = false;
    }, error => {
      window.alert("ID -->" + this.flowershopId);
    }
    );
  }




}
