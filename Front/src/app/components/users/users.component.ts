import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Importa Validators y FormGroup


@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})

export class UsersComponent implements OnInit {
  users: any[] = [];
  editingUser: any;
  userForm!: FormGroup; // Cambia el nombre de la variable a userForm

  constructor(private http: HttpClient, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.getUsers();
  }

  getUsers() {
    this.http.get('http://localhost:5000/users').subscribe((data: any) => {
      this.users = data;
    });
  }

  editUser(user: any) {
    this.editingUser = { ...user };
    this.userForm = this.formBuilder.group({
      username: [this.editingUser.username, Validators.required],
      phone: [this.editingUser.phone, [Validators.required, Validators.pattern('^[0-9]*$')]],
      state: [this.editingUser.state, Validators.required],
    });
  }

  updateUser() {
    if (this.editingUser && this.userForm.valid) {
      this.editingUser = { ...this.editingUser, ...this.userForm.value };
      this.http.put(`http://localhost:5000/users/update/id/${this.editingUser.userid}`, this.editingUser)
        .subscribe((response: any) => {
          if (response.message === "User updated successfully") {
            const index = this.users.findIndex(user => user.userid === this.editingUser.userid);
            this.users[index] = { ...this.editingUser };
            this.editingUser = null;
            this.userForm.reset(); // Limpia el formulario
          }
        });
    }
  }

  cancelEdit() {
    this.editingUser = null;
    this.userForm.reset(); // Limpia el formulario
  }
}