import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateFlowershopComponent } from './create-flowershop.component';

describe('CreateFlowershopComponent', () => {
  let component: CreateFlowershopComponent;
  let fixture: ComponentFixture<CreateFlowershopComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateFlowershopComponent]
    });
    fixture = TestBed.createComponent(CreateFlowershopComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
