import { Component } from '@angular/core';
import jwtDecode from 'jwt-decode';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { OnInit } from '@angular/core';



@Component({
  selector: 'app-my-employees',
  templateUrl: './my-employees.component.html',
  styleUrls: ['./my-employees.component.css']
})
export class MyEmployeesComponent implements OnInit{

  flowershopId: any = 0;
  users: any = {};
  inEditModeIndex: number = -1

  constructor(private router : Router, private http : HttpClient ) { }

  enterEditMode(i:any)
  {
    this.inEditModeIndex = i;
  }

  getFlowerShopID(){
    const token: any = localStorage.getItem('token');
    const tokenDesencripted: any = jwtDecode(token);
    this.flowershopId = tokenDesencripted.user.idflowershops;
  }

  getEmployees(): void {
    this.http.get(`http://localhost:5000/users/idflowershops/${this.flowershopId}`).subscribe((data: any) => {
      this.users= data;
      console.log(this.users[2]);
      console.log(data);
    }, error => {
      console.log(error);
    }
    );

  
  }


  ngOnInit(): void {
    this.getFlowerShopID();
    this.getEmployees();
  }

  editUser(id: any,i: any){
    this.http.put(`http://localhost:5000/users/update/id/${id}`, this.users[i]).subscribe((data: any) => {
      this.users = data;
      console.log(this.users);
      window.alert("User updated successfully");
      this.getEmployees();
      this.inEditModeIndex = -1;
    }, error => {
      console.log(error);
    }
    );

  }


  }

