import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { HomeComponent } from './components/home/home.component';
import { FlowershopsComponent } from './components/flowershops/flowershops.component';
import { CreateFlowershopComponent } from './components/create-flowershop/create-flowershop.component';
import { UsersComponent } from './components/users/users.component';
import { TokenGuardAdmin } from './guards/admin.guard';
import { TokenGuardOwner } from './guards/owner.guard';
import { TokenGuardBoss } from './guards/boss.guard';
import { TokenGuardFlowershop } from './guards/flowershop.guard';
import { CreateUserComponent } from './components/create-user/create-user.component';
import {OwnerViewComponent} from './components/owner-view/owner-view.component';
import {MyFlowershopComponent} from './components/my-flowershop/my-flowershop.component';
import {MyEmployeesComponent} from './components/my-employees/my-employees.component';
import {AdminViewComponent} from './components/admin-view/admin-view.component';
import {WarningComponent} from './components/warning/warning.component';
import { ProvidersComponent } from './components/providers/providers.component';
import { CreateProviderComponent } from './components/create-provider/create-provider.component'
import { ProductsComponent } from './components/products/products.component';
import { CreateProductComponent } from './components/create-product/create-product.component';
import { InventoryComponent } from './components/inventory/inventory.component';
import { MyInventoryComponent } from './components/my-inventory/my-inventory.component';
import { CreateInventoryComponent } from './components/create-inventory/create-inventory.component';
import { SalesComponent } from './components/sales/sales.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'flowershops', component: FlowershopsComponent, canActivate: [TokenGuardAdmin] },
  { path: 'flowershop/create', component: CreateFlowershopComponent, canActivate: [TokenGuardAdmin]},
  { path: 'users', component: UsersComponent, canActivate: [TokenGuardAdmin]},
  { path: 'user/create', component: CreateUserComponent, canActivate: [TokenGuardAdmin] },
  { path: 'owner', component: OwnerViewComponent, canActivate: [TokenGuardOwner] },
  { path: 'my-flowershop', component: MyFlowershopComponent, canActivate: [TokenGuardOwner]},
  { path: 'my-employees', component: MyEmployeesComponent, canActivate: [TokenGuardOwner]},
  { path: 'admin', component: AdminViewComponent, canActivate: [TokenGuardAdmin]},
  { path: 'providers', component: ProvidersComponent, canActivate: [TokenGuardBoss]},
  { path: 'provider/create', component: CreateProviderComponent, canActivate: [TokenGuardBoss]},
  { path: 'warning', component: WarningComponent},
  { path: 'products', component: ProductsComponent, canActivate: [TokenGuardBoss]},
  { path: 'product/create', component: CreateProductComponent, canActivate: [TokenGuardBoss]},
  { path: 'inventories', component: InventoryComponent, canActivate: [TokenGuardAdmin]},
  { path: 'my-inventories', component: MyInventoryComponent, canActivate: [TokenGuardFlowershop]},
  { path: 'inventory/create', component: CreateInventoryComponent, canActivate: [TokenGuardOwner]},
  { path: 'sale', component: SalesComponent, canActivate: [TokenGuardFlowershop]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
