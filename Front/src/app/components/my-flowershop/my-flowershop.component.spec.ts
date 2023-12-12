import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyFlowershopComponent } from './my-flowershop.component';

describe('MyFlowershopComponent', () => {
  let component: MyFlowershopComponent;
  let fixture: ComponentFixture<MyFlowershopComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MyFlowershopComponent]
    });
    fixture = TestBed.createComponent(MyFlowershopComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
