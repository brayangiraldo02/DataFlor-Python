import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FlowershopsComponent } from './flowershops.component';

describe('FlowershopsComponent', () => {
  let component: FlowershopsComponent;
  let fixture: ComponentFixture<FlowershopsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FlowershopsComponent]
    });
    fixture = TestBed.createComponent(FlowershopsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
