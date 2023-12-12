import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-owner-view',
  templateUrl: './owner-view.component.html',
  styleUrls: ['./owner-view.component.css']
})
export class OwnerViewComponent {

  constructor(private router: Router) { }

  navigateTo( route: string){
    this.router.navigate([route]);
  }

}
