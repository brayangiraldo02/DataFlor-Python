import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Importa Validators y FormGroup

@Component({
  selector: 'app-providers',
  templateUrl: './providers.component.html',
  styleUrls: ['./providers.component.css'] // Agrega el archivo CSS si lo tienes
})

export class ProvidersComponent implements OnInit {
  providers: any[] = [];
  selectedProvider: any;
  isEditing: boolean = false;
  providerForm!: FormGroup;

  constructor(private http: HttpClient, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.getProviders();
  }

  getProviders() {
    this.http.get('http://localhost:5000/providers')
      .subscribe((data: any) => {
        this.providers = data.sort((a: any, b: any) => b.state - a.state);
      });
  }

  editProvider(provider: any) {
    this.selectedProvider = { ...provider };
    this.isEditing = true;

    this.providerForm = this.formBuilder.group({
      fullname: [this.selectedProvider.fullname, [Validators.required, Validators.pattern('^[a-zA-Z ]*$')]],
      address: [this.selectedProvider.address, Validators.required],
      phone: [this.selectedProvider.phone, [Validators.required, Validators.pattern('^[0-9]*$')]],
      state: [this.selectedProvider.state, Validators.required],
    });
  }

  saveChanges() {
    if (this.selectedProvider && this.providerForm.valid) {
      this.selectedProvider = { ...this.selectedProvider, ...this.providerForm.value };
      
      this.http.put(`http://localhost:5000/providers/update/id/${this.selectedProvider.providerid}`, this.selectedProvider)
        .subscribe((data: any) => {
          this.getProviders();
          this.selectedProvider = null;
          this.isEditing = false;
        });
    }
  }

  cancelEdit() {
    this.selectedProvider = null;
    this.isEditing = false;
  }
}
