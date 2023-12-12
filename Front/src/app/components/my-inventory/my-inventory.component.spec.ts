import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyInventoryComponent } from './my-inventory.component';

describe('MyInventoryComponent', () => {
  let component: MyInventoryComponent;
  let fixture: ComponentFixture<MyInventoryComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MyInventoryComponent]
    });
    fixture = TestBed.createComponent(MyInventoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
