import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateDatasetPageComponent } from './create-dataset-page.component';

describe('DatasetPageComponent', () => {
  let component: CreateDatasetPageComponent;
  let fixture: ComponentFixture<CreateDatasetPageComponent>;
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateDatasetPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateDatasetPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
