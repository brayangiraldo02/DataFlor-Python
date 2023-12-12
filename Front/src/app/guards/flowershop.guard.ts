import { Router } from '@angular/router';
import decodeToken from 'jwt-decode';
import { CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

export class TokenGuardFlowershop implements CanActivate {
  constructor(private router: Router) { }

   canActivate(): boolean {
    const token:any = localStorage.getItem('token')
    if(token !== null){
      const tokenDesencripted:any  = decodeToken(token)
      if (tokenDesencripted.user.role === 'Dueño' || tokenDesencripted.user.role === 'Empleado') {
        return true;
      } else {
        this.router.navigate(['./warning']);
        return false;
      }
    } else {
      this.router.navigate(['./warning']);
      return false;
    }
  }
}