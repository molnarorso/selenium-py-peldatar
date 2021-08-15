var args = arguments,
  source = args[0],
  target = args[1],
  offsetX = args.length > 3 && args[2] || 0.5,
  offsetY = args.length > 4 && args[3] || 0.5,
  delay = args.length > 5 && args[4] || 1,
  callback = args[args.length - 1];

if (!source.draggable)
  throw 'Source element is not draggable.';

var doc = source.ownerDocument,
  rect1 = source.getBoundingClientRect(),
  rect2 = target ? target.getBoundingClientRect() : null,
  x = rect1.left + (rect1.width / 2),
  y = rect1.top + (rect1.height / 2),
  x2 = rect2 ? rect2.left + ((offsetX | 0) || offsetX * rect2.width) : x + offsetX,
  y2 = rect2 ? rect2.top + ((offsetY | 0) || offsetY * rect2.height) : y + offsetY,
  dataTransfer = Object.create(Object.prototype, {
    _items: { value: { } },
    effectAllowed: { value: 'all', writable: true },
    dropEffect: { value: 'move', writable: true },
    files: { get: function () { return undefined } },
    types: { get: function () { return Object.keys(this._items) } },
    setData: { value: function (format, data) { this._items[format] = data } },
    getData: { value: function (format) { return this._items[format] } },
    clearData: { value: function (format) { delete this._items[format] } },
    setDragImage: { value: function () { } }
  });

if(!(target = doc.elementFromPoint(x2, y2)))
  throw 'The target element is not interactable and need to be scrolled into the view.';

rect2 = target.getBoundingClientRect();

emit(source, 'dragstart', delay, function () {
  var rect3 = target.getBoundingClientRect();
  x = rect3.left + x2 - rect2.left;
  y = rect3.top + y2 - rect2.top;
  emit(target, 'dragenter', 1, function () {
    emit(target, 'dragover', delay, function () {
      target = doc.elementFromPoint(x, y);
      emit(target, 'drop', 1, function () {
        emit(source, 'dragend', 1, function () {
          callback();
});});});});});

function emit(element, type, delay, callback) {
  var event = doc.createEvent('DragEvent');
  event.initMouseEvent(type, true, true, doc.defaultView, 0, 0, 0, x, y, false, false, false, false, 0, null);
  Object.defineProperty(event, 'dataTransfer', { get: function () { return dataTransfer } });
  element.dispatchEvent(event);
  doc.defaultView.setTimeout(callback, delay);
}

